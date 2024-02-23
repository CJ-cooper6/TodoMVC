import { defineConfig } from "vite";
import vue from '@vitejs/plugin-vue';
 
export default defineConfig({
  plugins: [vue()],
  server: {
    host: "0.0.0.0",
    port: '5174',
    https: false,
    proxy: {
      "/api": {
        target: "http://host.docker.internal:5002",
        changeOrigin: true,
        ws: true,
      }
    },
  },
});