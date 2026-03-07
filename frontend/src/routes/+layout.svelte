<script lang="ts">
	/**
	 * Root layout — wraps every page.
	 *
	 * Responsibilities:
	 *  - Import global CSS (design tokens, reset, shared utilities)
	 *  - Wire up IntersectionObserver for .reveal scroll animations
	 *    after each navigation so new page elements are picked up.
	 */
	import { onMount } from 'svelte';
	import { afterNavigate } from '$app/navigation';
	import '../lib/styles/global.css';

	let { children } = $props();

	/** Attach IntersectionObserver to all .reveal elements on the current page. */
	function initReveal() {
		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						entry.target.classList.add('visible');
						// Unobserve after revealing — animation only happens once
						observer.unobserve(entry.target);
					}
				});
			},
			{ threshold: 0.12 }
		);

		document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
	}

	// Run on initial mount and after every client-side navigation
	onMount(initReveal);
	afterNavigate(initReveal);
</script>

{@render children?.()}
