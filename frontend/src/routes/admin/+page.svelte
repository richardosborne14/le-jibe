<script lang="ts">
	/**
	 * Admin login page — /admin
	 *
	 * Accepts the shared admin token (from ADMIN_TOKEN env var, passed
	 * to the API via Authorization header by all admin endpoints).
	 *
	 * On success: validates by calling GET /api/admin/signups (cheap check),
	 * stores token in sessionStorage, redirects to /admin/signups.
	 *
	 * On failure: shows inline error message.
	 */
	import { goto } from '$app/navigation';

	let token = $state('');
	let loading = $state(false);
	let errorMsg = $state('');

	/** Validate the token against a real admin endpoint. */
	async function handleLogin(event: SubmitEvent) {
		event.preventDefault();
		if (!token.trim()) return;

		loading = true;
		errorMsg = '';

		try {
			// Use a lightweight admin endpoint to verify the token
			const res = await fetch('/api/admin/signups', {
				headers: { Authorization: `Bearer ${token.trim()}` },
			});

			if (res.ok) {
				// Token is valid — persist and navigate to dashboard
				sessionStorage.setItem('admin_token', token.trim());
				goto('/admin/signups');
			} else if (res.status === 401 || res.status === 403) {
				errorMsg = 'Token incorrect. Vérifiez la valeur ADMIN_TOKEN.';
			} else {
				errorMsg = `Erreur inattendue (${res.status}). Réessayez.`;
			}
		} catch {
			errorMsg = 'Impossible de joindre le serveur. Vérifiez que le backend tourne.';
		} finally {
			loading = false;
		}
	}
</script>

<svelte:head>
	<title>Admin — Le Jibé</title>
</svelte:head>

<main class="login-main">
	<div class="login-card">
		<div class="login-logo">Le <span>Jibé</span></div>
		<p class="login-subtitle">Accès administration</p>

		<form onsubmit={handleLogin}>
			<div class="form-group">
				<label class="form-label" for="admin-token">Token d'accès</label>
				<input
					class="form-input"
					id="admin-token"
					type="password"
					placeholder="••••••••••••"
					bind:value={token}
					disabled={loading}
					autocomplete="current-password"
					required
				/>
			</div>

			{#if errorMsg}
				<div class="login-error" role="alert">{errorMsg}</div>
			{/if}

			<button type="submit" class="btn-login" disabled={loading || !token.trim()}>
				{loading ? 'Vérification…' : 'Connexion →'}
			</button>
		</form>

		<p class="login-note">Session active jusqu'à la fermeture de l'onglet.</p>
	</div>
</main>

<style>
	.login-main {
		min-height: 100vh;
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 2rem;
		background: var(--ink);
	}

	.login-card {
		width: 100%;
		max-width: 400px;
		background: var(--ink-soft);
		border: 1px solid rgba(245, 240, 232, 0.08);
		border-radius: 4px;
		padding: 2.5rem;
	}

	.login-logo {
		font-family: var(--f-display);
		font-weight: 800;
		font-size: 1.5rem;
		letter-spacing: 0.05em;
		color: var(--white);
		margin-bottom: 0.25rem;
	}

	.login-logo span {
		color: var(--amber);
	}

	.login-subtitle {
		font-size: 0.78rem;
		color: var(--muted);
		letter-spacing: 0.08em;
		text-transform: uppercase;
		margin-bottom: 2rem;
	}

	.form-group {
		display: flex;
		flex-direction: column;
		gap: 0.4rem;
		margin-bottom: 1rem;
	}

	.login-error {
		background: rgba(224, 82, 82, 0.08);
		border: 1px solid rgba(224, 82, 82, 0.3);
		border-radius: 2px;
		padding: 0.75rem 1rem;
		font-size: 0.82rem;
		color: #e05252;
		margin-bottom: 1rem;
	}

	.btn-login {
		width: 100%;
		font-family: var(--f-display);
		font-weight: 700;
		font-size: 0.82rem;
		letter-spacing: 0.14em;
		text-transform: uppercase;
		padding: 0.9rem;
		background: var(--amber);
		color: var(--ink);
		border: none;
		border-radius: 2px;
		cursor: pointer;
		transition: background 0.2s;
		margin-bottom: 1.25rem;
	}

	.btn-login:hover:not(:disabled) {
		background: var(--amber-bright);
	}

	.btn-login:disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}

	.login-note {
		font-size: 0.7rem;
		color: rgba(138, 133, 120, 0.6);
		text-align: center;
	}
</style>
