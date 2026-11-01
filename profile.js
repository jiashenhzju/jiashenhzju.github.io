// Native dialog provides focus containment, Escape dismissal, and focus return.
const wechatTrigger = document.getElementById('wechat-qr-trigger');
const wechatDialog = document.getElementById('wechat-qr-modal');

if (wechatTrigger && wechatDialog) {
  wechatTrigger.addEventListener('click', () => wechatDialog.showModal());
  wechatDialog.querySelector('.wechat-qr-modal-close').addEventListener('click', () => wechatDialog.close());
  wechatDialog.addEventListener('click', (event) => {
    if (event.target !== wechatDialog) return;
    const bounds = wechatDialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right ||
        event.clientY < bounds.top || event.clientY > bounds.bottom) {
      wechatDialog.close();
    }
  });
}
