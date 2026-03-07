<script lang="ts">
	/**
	 * Admin layout — auth guard for all /admin/* routes.
	 *
	 * Token is stored in sessionStorage (clears on tab close — intentional
	 * for admin security without a full auth system).
	 *
	 * If no token is found on a protected page, redirects to /admin login.
	 * We check window.location.pathname (safe inside onMount) rather than
	 * the typed page store to avoid SvelteKit's strict route-typing issues.
	 */
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';

	let { children } = $props();

	let checking = $state(true);

	onMount(() => {
		const token = sessionStorage.getItem('admin_token');
		const isLoginPage = window.location.pathname === '/admin';

		if (!token && !isLoginPage) {
			// No token and not on login page — redirect to login
			goto('/admin');
		}

		checking = false;
	});
</script>

{#if checking}
	<!-- Brief invisible state while auth check runs — prevents flash of protected content -->
	<div style="display:none" aria-hidden="true"></div>
{:else}
	{@render children?.()}
{/if}
