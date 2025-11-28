(function(global){
  const ProgressTracker = {
    _defaults: {
      storagePrefix: 'edu_progress_',
      throttleMs: 150
    },
    _uiRefs: {},
    _throttleTimers: {},
    initSummaryUI(opts = {}) {
      this._uiRefs.summary = opts;
      this.updateUIFromStorage();
      window.addEventListener('storage', (e)=> {
        if(e.key && e.key.startsWith(this._defaults.storagePrefix)) {
          this.updateUIFromStorage();
        }
      });
    },

    bindChapter({ articleSelector, topBar, percentNode, statusNode, storageKey='edu_progress_ch1', markWhen=0.995 }) {
      // articleSelector: selector for article element
      const art = document.querySelector(articleSelector);
      if(!art) return console.warn('ProgressTracker: article not found', articleSelector);
      // update UI from current storage
      this._uiRefs[storageKey] = { topBar, percentNode, statusNode, storageKey, markWhen };
      // throttled scroll handler
      let ticking = false;
      const saveKey = (k, v) => {
        localStorage.setItem(k, String(v));
        window.dispatchEvent(new Event('progress:updated'));
      };

      const calcAndSave = ()=> {
        // compute scroll progress within article (0..1)
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        const rect = art.getBoundingClientRect();
        // compute how far user has scrolled within the article element
        const docTop = scrollTop + rect.top; // top position of article relative to document
        const readY = (scrollTop - docTop) + window.innerHeight; // visible portion relative
        const total = art.scrollHeight;
        let p = (readY / total);
        p = Math.min(Math.max(p, 0), 1);
        const percent = Math.round(p*100);

        saveKey(storageKey, percent);
        // if percent >= markWhen*100 then set to 100
        if(p >= markWhen) saveKey(storageKey, 100);
        // update UI for this page
        this._applyUI(storageKey, percent);
      };

      const onScroll = ()=> {
        if(this._throttleTimers[storageKey]) return;
        this._throttleTimers[storageKey] = setTimeout(()=>{
          this._throttleTimers[storageKey] = null;
          calcAndSave();
        }, this._defaults.throttleMs);
      };

      // initial
      calcAndSave();
      // listeners
      window.addEventListener('scroll', onScroll, { passive:true });
      window.addEventListener('resize', onScroll);
      // also respond to storage changes from other tabs
      window.addEventListener('storage', (e)=>{
        if(e.key === storageKey) {
          // update UI to reflect remote change
          const val = Number(localStorage.getItem(storageKey) || 0);
          this._applyUI(storageKey, val);
        }
      });

      // convenience: expose a setProgress method
      // for example: ProgressTracker.setProgress('edu_progress_ch1', 100)
    },

    _applyUI(storageKey, percent){
      const refs = this._uiRefs[storageKey];
      if(!refs) return;
      // topBar
      try{
        if(refs.topBar){
          const el = document.querySelector(refs.topBar);
          if(el) el.style.width = (percent)+'%';
        }
        if(refs.percentNode){
          const n = document.querySelector(refs.percentNode);
          if(n) n.textContent = (percent)+'%';
        }
        if(refs.statusNode){
          const s = document.querySelector(refs.statusNode);
          if(s) s.textContent = percent >= 100 ? 'Selesai' : 'Belum selesai';
        }
      }catch(err){ console.warn(err); }
      // update summary as well
      this.updateUIFromStorage();
    },

    updateUIFromStorage(){
      // read all edu_progress_* keys, populate summary bars
      const keys = Object.keys(localStorage).filter(k=>k.startsWith(this._defaults.storagePrefix));
      // ch1..ch3
      const ch1 = Number(localStorage.getItem('edu_progress_ch1') || 0);
      const ch2 = Number(localStorage.getItem('edu_progress_ch2') || 0);
      const ch3 = Number(localStorage.getItem('edu_progress_ch3') || 0);
      // update summary UI if available
      const s = this._uiRefs.summary || {};
      if(s.ch1Bar) { const el = document.querySelector(s.ch1Bar); if(el) el.style.width = ch1+'%'; }
      if(s.ch1Val) { const el = document.querySelector(s.ch1Val); if(el) el.textContent = ch1+'%'; }
      if(s.ch2Bar) { const el = document.querySelector(s.ch2Bar); if(el) el.style.width = ch2+'%'; }
      if(s.ch2Val) { const el = document.querySelector(s.ch2Val); if(el) el.textContent = ch2+'%'; }
      if(s.ch3Bar) { const el = document.querySelector(s.ch3Bar); if(el) el.style.width = ch3+'%'; }
      if(s.ch3Val) { const el = document.querySelector(s.ch3Val); if(el) el.textContent = ch3+'%'; }
      // total average (only consider chapters that exist: use denominator 3)
      const total = Math.round((ch1 + ch2 + ch3) / 3);
      if(s.total) { const el = document.querySelector(s.total); if(el) el.textContent = total+'%'; }
      // also update any known chapter status nodes stored in _uiRefs
      Object.keys(this._uiRefs).forEach(k=>{
        if(k.startsWith(this._defaults.storagePrefix) === false && k.startsWith('edu_progress_')===false) return;
      });
    },

    setProgress(key, percent){
      localStorage.setItem(key, String(percent));
      // manual apply
      this.updateUIFromStorage();
      window.dispatchEvent(new Event('progress:updated'));
    },

    resetAll(){
      // remove keys that start with prefix
      const keys = Object.keys(localStorage).filter(k => k.startsWith(this._defaults.storagePrefix));
      keys.forEach(k=> localStorage.removeItem(k));
      this.updateUIFromStorage();
    }
  };

  // expose to global
  global.ProgressTracker = ProgressTracker;

})(window);
