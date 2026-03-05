import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		host: '0.0.0.0',
		port: 5173,
		// Allow HMR to work when accessed via nginx on port 80
		hmr: {
			clientPort: 5173
		}
	}
});
