const gridEl = document.getElementById('grid');
const statusEl = document.getElementById('status');
const refreshBtn = document.getElementById('refresh-btn');
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const lightboxCaption = document.getElementById('lightbox-caption');
const lightboxClose = document.getElementById('lightbox-close');

function imageUrl(name) {
  return `/images/${encodeURIComponent(name)}`;
}

async function fetchImages() {
  const res = await fetch('/api/images');
  if (!res.ok) throw new Error(`Server error (${res.status})`);
  return res.json();
}

function renderGrid(files) {
  gridEl.innerHTML = '';
  for (const file of files) {
    const card = document.createElement('button');
    card.className = 'card';
    card.type = 'button';

    const img = document.createElement('img');
    img.loading = 'lazy';
    img.src = imageUrl(file.name);
    img.alt = file.name;

    const caption = document.createElement('span');
    caption.className = 'caption';
    caption.textContent = file.name;

    card.append(img, caption);
    card.addEventListener('click', () => openLightbox(file));
    gridEl.append(card);
  }
}

function openLightbox(file) {
  lightboxImg.src = imageUrl(file.name);
  lightboxImg.alt = file.name;
  lightboxCaption.textContent = file.name;
  lightbox.hidden = false;
}

function closeLightbox() {
  lightbox.hidden = true;
  lightboxImg.src = '';
}

lightboxClose.addEventListener('click', closeLightbox);
lightbox.addEventListener('click', (event) => {
  if (event.target === lightbox) closeLightbox();
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') closeLightbox();
});

async function load() {
  statusEl.textContent = 'Loading images…';
  refreshBtn.disabled = true;
  try {
    const files = await fetchImages();
    renderGrid(files);
    statusEl.textContent = files.length
      ? `${files.length} image${files.length === 1 ? '' : 's'}`
      : 'No images found in this folder yet.';
  } catch (err) {
    console.error(err);
    statusEl.textContent = `⚠️ ${err.message}`;
  } finally {
    refreshBtn.disabled = false;
  }
}

refreshBtn.addEventListener('click', load);
load();
