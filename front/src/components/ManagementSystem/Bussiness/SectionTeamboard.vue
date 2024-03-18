<template>
  <!-- <iframe
    title="X-section teamboard"
    width="1220"
    height="700"
    src="https://app.powerbi.com/reportEmbed?reportId=efd8d718-c732-41b7-a013-e8c6c25741d7&autoAuth=true&ctid=0ae51e19-07c8-4e4b-bb6d-648ee58410f4"
    frameborder="0"
    allowFullScreen="true"
  ></iframe> -->

  <iframe
    id="powerbi-iframe"
    title="X-section teamboard"
    src="https://app.powerbi.com/reportEmbed?reportId=10ae3bd2-c57a-4abc-b0d6-c76639704e7d&autoAuth=true&ctid=0ae51e19-07c8-4e4b-bb6d-648ee58410f4"
    frameborder="0"
    allowfullscreen="true"
    style="width: 100%; height: 730px"
  ></iframe>
</template>

<script>
export default {
  mounted() {
    this.adjustIframeSize();
    window.addEventListener("resize", this.adjustIframeSize);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.adjustIframeSize);
  },
  methods: {
    adjustIframeSize() {
      const iframe = document.getElementById("powerbi-iframe");
      if (iframe) {
        // 调整高度，例如设置为视窗高度的一定比例
        iframe.style.height = window.innerHeight * 0.8 + "px";
      }
    },
  },
};
</script>
