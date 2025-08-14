// Xử lý autoplay và mute trên iOS/Android
document.addEventListener("DOMContentLoaded", () => {
  const video = document.querySelector("#ar-video");
  const sceneEl = document.querySelector("a-scene");
  const unmuteBtn = document.getElementById("unmuteBtn");

  // iOS yêu cầu muted + playsinline để autoplay
  video.muted = true;
  video.setAttribute("playsinline", "");
  video.setAttribute("webkit-playsinline", "");

  // Khi theo dõi được ảnh mục tiêu thì phát video, mất mục tiêu thì tạm dừng
  sceneEl.addEventListener("targetFound", () => {
    // Rewind nhẹ để đảm bảo khởi đầu khi bắt được marker
    if (video.currentTime < 0.01) {
      try { video.currentTime = 0; } catch {}
    }
    video.play().catch(() => {});
  });

  sceneEl.addEventListener("targetLost", () => {
    if (!video.paused) video.pause();
  });

  // Nút bật tiếng khi người dùng đã tương tác
  unmuteBtn.addEventListener("click", () => {
    video.muted = false;
    video.play().catch(() => {});
    unmuteBtn.style.display = "none";
  });

  // Một số trình duyệt yêu cầu chạm lần đầu
  document.body.addEventListener("touchstart", () => {
    video.play().catch(() => {});
  }, { once: true });
});
