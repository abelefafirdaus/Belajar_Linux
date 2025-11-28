/* ======================================================
 *  LinuxEdu Terminal Simulator (Ubuntu Style)
 *  Dibuat dengan prinsip Software Quality Assurance (SQA)
 *  & Rekayasa Perangkat Lunak Modular
 * ====================================================== */

document.addEventListener("DOMContentLoaded", () => {
  const terminalOutput = document.getElementById("terminalOutput");
  const terminalInput = document.getElementById("terminalInput");

  const ubuntuPrompt = "student@linuxedu:~$ ";

  // ==== INITIAL OUTPUT ====
  printOutput("Ubuntu Linux Terminal Emulator — LinuxEdu v1.0");
  printOutput("Ketik <code>help</code> untuk melihat daftar perintah yang tersedia.\n");

  // ==== COMMAND HANDLER ====
  terminalInput.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      e.preventDefault();
      const command = terminalInput.value.trim();
      if (command) {
        printCommand(command);
        processCommand(command);
      }
      terminalInput.value = "";
    }
  });

  // ==== FUNCTION: PRINT COMMAND ====
  function printCommand(command) {
    const div = document.createElement("div");
    div.innerHTML = `<span class="text-success">${ubuntuPrompt}</span>${escapeHtml(command)}`;
    terminalOutput.appendChild(div);
    terminalOutput.scrollTop = terminalOutput.scrollHeight;
  }

  // ==== FUNCTION: PRINT OUTPUT ====
  function printOutput(text) {
    const div = document.createElement("div");
    div.innerHTML = text.replace(/\n/g, "<br>");
    terminalOutput.appendChild(div);
    terminalOutput.scrollTop = terminalOutput.scrollHeight;
  }

  // ==== FUNCTION: ESCAPE HTML ====
  function escapeHtml(unsafe) {
    return unsafe.replace(/[&<"']/g, m => ({ '&': '&amp;', '<': '&lt;', '"': '&quot;', "'": '&#039;' }[m]));
  }

  // ==== FUNCTION: PROCESS COMMAND ====
  function processCommand(command) {
    const args = command.split(" ");
    const cmd = args[0].toLowerCase();

    switch (cmd) {
      case "help":
        printOutput(`
<b>Daftar Perintah Tersedia:</b><br>
<code>help</code> — menampilkan daftar perintah<br>
<code>clear</code> — membersihkan layar terminal<br>
<code>ls</code> — menampilkan daftar direktori<br>
<code>pwd</code> — menampilkan direktori saat ini<br>
<code>cat</code> [file] — membaca isi file dummy<br>
<code>sudo apt install</code> [paket] — simulasi instalasi<br>
<code>echo</code> [teks] — menampilkan teks kembali<br>
`);
        break;

      case "clear":
        terminalOutput.innerHTML = "";
        break;

      case "ls":
        printOutput(`Documents  Downloads  Music  Pictures  Videos  <span class="text-info">ubuntu.txt</span>`);
        break;

      case "pwd":
        printOutput("/home/student");
        break;

      case "cat":
        if (args[1] === "ubuntu.txt") {
          printOutput(`Ubuntu adalah sistem operasi berbasis Linux yang ramah pengguna dan open-source.🐧`);
        } else {
          printOutput("cat: file tidak ditemukan.");
        }
        break;

      case "sudo":
        if (args[1] === "apt" && args[2] === "install" && args[3]) {
          simulateInstall(args[3]);
        } else {
          printOutput("Perintah sudo tidak lengkap atau salah.");
        }
        break;

      case "echo":
        printOutput(command.replace("echo", "").trim());
        break;

      default:
        printOutput(`bash: ${cmd}: command not found`);
        break;
    }
  }

  // ==== FUNCTION: SIMULATE INSTALL ====
  function simulateInstall(pkgName) {
    const steps = [
      `[sudo] password for student: ********`,
      `Reading package lists... Done`,
      `Building dependency tree... Done`,
      `Reading state information... Done`,
      `The following NEW packages will be installed:`,
      `  ${pkgName}`,
      `After this operation, 5 MB of additional disk space will be used.`,
      `Do you want to continue? [Y/n]`
    ];

    let i = 0;
    const interval = setInterval(() => {
      if (i < steps.length) {
        printOutput(steps[i]);
        i++;
      } else {
        clearInterval(interval);
        setTimeout(() => {
          printOutput(`\nSetting up ${pkgName} (1.0.0)... Done`);
          printOutput(`${pkgName} installed successfully ✅`);
        }, 500);
      }
    }, 400);
  }
});
