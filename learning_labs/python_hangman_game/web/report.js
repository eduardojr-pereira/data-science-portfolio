'use strict';
(() => {
  const WORDS = ['FORMIGA','BABUINO','ENCEFALO','ELEFANTE','GIRAFA','HAMBURGUER','CHOCOLATE','GIROSCOPIO'];
  const MAX_ERRORS = 6;
  const txt = {
    pt: {eyebrow:'Laboratório de Python',title:'Jogo da Forca',intro:'Descubra a palavra antes que suas seis tentativas acabem.',solo:'Um jogador',duo:'Dois jogadores',secret:'Jogador 1: escolha a palavra secreta',begin:'Iniciar partida',new:'Nova partida',restart:'Jogar novamente',attempts:'Erros',misses:'Letras erradas',none:'nenhuma',keyboard:'Escolha uma letra no teclado virtual ou físico.',ready:'Partida iniciada. Boa sorte!',correct:'Boa! Letra encontrada.',incorrect:'Essa letra não aparece na palavra.',repeated:'Você já tentou essa letra.',win:'Você venceu! Palavra: ',lose:'Fim de jogo! Palavra: ',invalid:'Use somente letras, sem espaços nem números.',enter:'Digite uma palavra para começar.',inputLabel:'Palavra secreta',inputPlaceholder:'Palavra secreta',notice:'Os dois modos funcionam inteiramente no navegador. No modo para dois jogadores, o Jogador 1 deve digitar a palavra sem que o Jogador 2 veja.',help:'Acentos são normalizados; letras repetidas não gastam tentativas.',modePrompt:'Selecione um modo para começar.',showcase:'Vitrine'},
    en: {eyebrow:'Python Learning Lab',title:'Hangman Game',intro:'Guess the hidden word before your six attempts run out.',solo:'Single player',duo:'Two players',secret:'Player 1: choose a secret word',begin:'Start game',new:'New game',restart:'Play again',attempts:'Mistakes',misses:'Incorrect letters',none:'none',keyboard:'Choose a letter using the on-screen or physical keyboard.',ready:'Game started. Good luck!',correct:'Great! Letter found.',incorrect:'That letter is not in the word.',repeated:'You already tried that letter.',win:'You win! Word: ',lose:'Game over! Word: ',invalid:'Use letters only, no spaces or numbers.',enter:'Enter a word to begin.',inputLabel:'Secret word',inputPlaceholder:'Secret word',notice:'Both modes run entirely in your browser. In two-player mode, Player 1 should enter a word privately.',help:'Accents are normalized; repeated guesses do not count as mistakes.',modePrompt:'Select a mode to begin.',showcase:'Showcase'}
  };
  const el = id => document.getElementById(id);
  const buttons = Array.from(document.querySelectorAll('[data-letter]'));
  const normalize = value => String(value).trim().normalize('NFD').replace(/[\u0300-\u036f]/g,'').toUpperCase();
  const isValidWord = value => /^[A-Z]+$/.test(value);
  let lang = 'pt', mode = 'solo', secret = '', correct = new Set(), wrong = [], state = 'playing', previousIndex = -1;
  const t = key => txt[lang][key];
  const newWord = () => {
    let i;
    if (window.crypto?.getRandomValues) {
      const arr = new Uint32Array(1);
      const cutoff = 0x100000000 - (0x100000000 % WORDS.length);
      do { window.crypto.getRandomValues(arr); } while(arr[0] >= cutoff);
      i = arr[0] % WORDS.length;
    } else { i = Math.floor(Math.random() * WORDS.length); }
    if (WORDS.length > 1 && i === previousIndex) i = (i + 1) % WORDS.length;
    previousIndex = i;
    return WORDS[i];
  };
  function status(message, kind='neutral') { const node=el('status'); node.textContent=message;node.dataset.state=kind; }
  function updateText() {
    document.documentElement.lang = lang === 'pt' ? 'pt-BR' : 'en';
    document.title = `${t('title')} · EP Learning Lab`;
    for (const node of document.querySelectorAll('[data-i18n]')) node.textContent=t(node.dataset.i18n);
    el('secret').setAttribute('aria-label',t('inputLabel'));
    el('secret').placeholder=t('inputPlaceholder');
    el('locale-pt').setAttribute('aria-pressed',String(lang==='pt'));
    el('locale-en').setAttribute('aria-pressed',String(lang==='en'));
    el('solo').classList.toggle('active',mode==='solo'); el('duo').classList.toggle('active',mode==='duo');
    el('solo').setAttribute('aria-pressed',String(mode==='solo'));el('duo').setAttribute('aria-pressed',String(mode==='duo'));
    el('secret-form').hidden=mode==='solo';
    render();
    if(state==='won')status(t('win')+secret+'.','win');
    else if(state==='lost')status(t('lose')+secret+'.','lose');
    else if(state==='setup')status(t('enter'));
    else status(t('ready'));
  }
  function render() {
    document.querySelectorAll('[data-part]').forEach(node=>node.classList.toggle('visible',Number(node.dataset.part)<=wrong.length));
    const word=el('word');word.replaceChildren();
    for(const letter of secret) {
      const slot=document.createElement('span');slot.className='letter-slot';
      const revealed=correct.has(letter) || state!=='playing';
      slot.textContent=revealed?letter:'\u00a0';
      slot.classList.toggle('revealed',revealed);word.append(slot);
    }
    el('mistake-count').textContent=`${wrong.length} / ${MAX_ERRORS}`;
    el('misses').textContent=wrong.join(', ') || t('none');
    buttons.forEach(node=>{const letter=node.dataset.letter;node.disabled=state!=='playing'||mode==='duo'&&!secret||correct.has(letter)||wrong.includes(letter);node.classList.toggle('hit',correct.has(letter));node.classList.toggle('miss',wrong.includes(letter));});
  }
  function start(value) {
    secret=normalize(value); if(!isValidWord(secret)){status(t('invalid'));el('secret').focus();return;}
    correct=new Set();wrong=[];state='playing'; el('secret').value='';
    render(); status(t('ready')); el('keyboard').focus({preventScroll:true});
  }
  function setMode(value){mode=value;secret='';correct=new Set();wrong=[];state='setup';updateText();if(mode==='solo')start(newWord());else {status(t('enter'));el('secret').focus();}}
  function guess(raw) {
    if(state!=='playing')return;
    const letter=normalize(raw);if(!/^[A-Z]$/.test(letter))return;
    if(correct.has(letter)||wrong.includes(letter)){status(t('repeated'));return;}
    if(secret.includes(letter))correct.add(letter);else wrong.push(letter);
    let kind='neutral',message=secret.includes(letter)?t('correct'):t('incorrect');
    if([...new Set(secret)].every(l=>correct.has(l))){state='won';kind='win';message=t('win')+secret+'.';}
    else if(wrong.length>=MAX_ERRORS){state='lost';kind='lose';message=t('lose')+secret+'.';}
    render();status(message,kind);
  }
  el('solo').addEventListener('click',()=>setMode('solo'));
  el('duo').addEventListener('click',()=>setMode('duo'));
  el('locale-pt').addEventListener('click',()=>{lang='pt';updateText();});
  el('locale-en').addEventListener('click',()=>{lang='en';updateText();});
  el('secret-form').addEventListener('submit',event=>{event.preventDefault();const value=el('secret').value;if(!value.trim()){status(t('enter'));return;}start(value);});
  el('restart').addEventListener('click',()=>setMode(mode));
  buttons.forEach(node=>node.addEventListener('click',()=>guess(node.dataset.letter)));
  document.addEventListener('keydown',event=>{
    if(event.ctrlKey||event.altKey||event.metaKey||event.isComposing)return;
    if(['INPUT','TEXTAREA','SELECT'].includes(event.target.tagName)||event.target.isContentEditable)return;
    if(/^[a-zA-Z]$/.test(event.key))guess(event.key);
  });

  // EP-HANGMAN-GITHUB-CLICK-V2: native click-only dropdown; close on outside click or Escape.
  const epGithubMenu = document.querySelector('.github-dropdown');
  if(epGithubMenu) {
    const epGithubSummary = epGithubMenu.querySelector('summary');
    document.addEventListener('pointerdown', event => {
      if(!epGithubMenu.contains(event.target)) epGithubMenu.open=false;
    });
    document.addEventListener('keydown', event => {
      if(event.key==='Escape' && epGithubMenu.open) {
        epGithubMenu.open=false;
        epGithubSummary.focus();
      }
    });
  }
  setMode('solo');
})();
