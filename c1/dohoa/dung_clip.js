// Dựng thẻ thử C1 thành 2 clip: WebM VP9 alpha và MP4 nền xanh lá.
// Bản MOV ProRes 4444 (khoảng 20 MB) do c1/chay_c1.py tự chuyển từ WebM trên máy Windows.
// Chạy: node c1/dohoa/dung_clip.js  (cần Playwright + FFmpeg)
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs'), path = require('path'), os = require('os');

const FPS = 30, GIAY = 3, HTML = path.resolve(__dirname, 'the_gia.html');
const RA = path.resolve(__dirname, '..', 'assets');

(async () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'c1-khung-'));
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + HTML);
  for (let i = 0; i < FPS * GIAY; i++) {
    await page.evaluate(t => window.datThoiGian(t), i / FPS);
    await page.screenshot({ path: path.join(tmp, `k${String(i).padStart(4, '0')}.png`), omitBackground: true });
  }
  await browser.close();
  const vao = ['-y', '-loglevel', 'error', '-framerate', String(FPS), '-i', path.join(tmp, 'k%04d.png')];
  fs.mkdirSync(RA, { recursive: true });
  execFileSync('ffmpeg', [...vao, '-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p', '-b:v', '2M', '-auto-alt-ref', '0', path.join(RA, 'the_gia_alpha.webm')]);
  execFileSync('ffmpeg', [...vao, '-f', 'lavfi', '-i', `color=c=0x00FF00:s=1080x1920:r=${FPS}:d=${GIAY}`,
    '-filter_complex', '[1][0]overlay=shortest=1,format=yuv420p', '-c:v', 'libx264', '-crf', '18', path.join(RA, 'the_gia_xanh.mp4')]);
  fs.rmSync(tmp, { recursive: true, force: true });
  console.log('Đã dựng xong 3 clip trong', RA);
})();
