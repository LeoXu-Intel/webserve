<template>
  <!-- <iframe
    title="ASIC&Power Teamboard"
    width="1220"
    height="730"
    src="https://app.powerbi.com/reportEmbed?reportId=4cd93958-79fa-4b78-ab61-f492ebb60b06&autoAuth=true&ctid=0ae51e19-07c8-4e4b-bb6d-648ee58410f4"
    frameborder="0"
    allowFullScreen="true"
  ></iframe> -->

  <iframe
    id="powerbi-iframe"
    title="ASIC&Power Teamboard"
    src="https://app.powerbi.com/reportEmbed?reportId=f44c8cd4-941c-4ae7-8d85-cce425e99abf&autoAuth=true&ctid=0ae51e19-07c8-4e4b-bb6d-648ee58410f4"
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
