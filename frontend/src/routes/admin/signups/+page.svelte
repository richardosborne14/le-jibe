<script lang="ts">
	/**
	 * Admin signups page — /admin/signups
	 *
	 * Displays all signups sorted by created_at desc.
	 * CSV export is client-side (Blob + URL.createObjectURL) — no server endpoint needed.
	 */
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';

	interface Signup {
		id: string;
		first_name: string;
		email: string;
		profile_type: string;
		created_at: string;
	}

	let signups: Signup[] = $state([]);
	let loading = $state(true);
	let fetchError = $state('');

	/** French labels for profile_type enum values. */
	const profileLabels: Record<string, string> = {
		user: 'Utilisateur',
		caregiver: 'Aidant / proche',
		professional: 'Professionnel de santé',
		other: 'Autre',
	};

	/** Format ISO date to French locale. */
	function formatDate(iso: string): string {
		return new Intl.DateTimeFormat('fr-FR', {
			day: '2-digit',
			month: '2-digit',
			year: 'numeric',
			hour: '2-digit',
			minute: '2-digit',
		}).format(new Date(iso));
	}

	/** Get stored admin token — redirect if missing. */
	function getToken(): string | null {
		const token = sessionStorage.getItem('admin_token');
		if (!token) goto('/admin');
		return token;
	}

	onMount(async () => {
		const token = getToken();
		if (!token) return;

		try {
			const res = await fetch('/api/admin/signups', {
				headers: { Authorization: `Bearer ${token}` },
			});

			if (res.status === 401 || res.status === 403) {
				sessionStorage.removeItem('admin_token');
				goto('/admin');
				return;
			}

			if (!res.ok) throw new Error(`HTTP ${res.status}`);
			signups = await res.json();
		} catch {
			fetchError = 'Erreur lors du chargement des inscriptions.';
		} finally {
			loading = false;
		}
	});

	/**
	 * Export signups as CSV.
	 * Generated entirely client-side — no additional API endpoint.
	 */
	function exportCsv() {
		const headers = ['ID', 'Prénom', 'Email', 'Profil', 'Date inscription'];
		const rows = signups.map((s) => [
			s.id,
			s.first_name,
			s.email,
			profileLabels[s.profile_type] ?? s.profile_type,
			formatDate(s.created_at),
		]);

		const csv = [headers, ...rows]
			.map((row) => row.map((cell) => `"${String(cell).replace(/"/g, '""')}"`).join(','))
			.join('\n');

		const blob = new Blob(['\uFEFF' + csv], { type: 'text/csv;charset=utf-8;' });
		const url = URL.createObjectURL(blob);
		const link = document.createElement('a');
		link.href = url;
		link.download = `lejibe-inscriptions-${new Date().toISOString().slice(0, 10)}.csv`;
		link.click();
		URL.revokeObjectURL(url);
	}

	function handleLogout() {
		sessionStorage.removeItem('admin_token');
		goto('/admin');
	}
</script>

<svelte:head>
	<title>Inscriptions — Admin Le Jibé</title>
</svelte:head>

<div class="admin-page">
	<!-- Admin nav -->
	<header class="admin-nav">
		<a href="/" class="admin-logo">Le <span>Jibé</span></a>
		<nav class="admin-links">
			<a href="/admin/signups" class="admin-link active">Inscriptions</a>
			<a href="/admin/posts" class="admin-link">Articles</a>
		</nav>
		<button class="btn-logout" onclick={handleLogout}>Déconnexion</button>
	</header>

	<main class="admin-main">
		<div class="page-header">
			<div>
				<h1 class="page-title">Inscriptions</h1>
				{#if !loading && !fetchError}
					<p class="count-badge">{signups.length} inscrits</p>
				{/if}
			</div>
			<button class="btn-export" onclick={exportCsv} disabled={signups.length === 0}>
				Exporter CSV →
			</button>
		</div>

		{#if loading}
			<div class="admin-loading">Chargement…</div>
		{:else if fetchError}
			<div class="admin-error" role="alert">{fetchError}</div>
		{:else if signups.length === 0}
			<div class="admin-empty">Aucune inscription pour le moment.</div>
		{:else}
			<div class="table-wrap">
				<table>
					<thead>
						<tr>
							<th>Prénom</th>
							<th>Email</th>
							<th>Profil</th>
							<th>Date</th>
						</tr>
					</thead>
					<tbody>
						{#each signups as signup}
							<tr>
								<td>{signup.first_name}</td>
								<td><a href="mailto:{signup.email}" class="email-link">{signup.email}</a></td>
								<td>
									<span class="profile-badge">
										{profileLabels[signup.profile_type] ?? signup.profile_type}
									</span>
								</td>
								<td class="date-cell">{formatDate(signup.created_at)}</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		{/if}
	</main>
</div>

<style>
	/* ── Admin shell ── */
	.admin-page {
		min-height: 100vh;
		background: var(--ink);
		display: flex;
		flex-direction: column;
	}

	.admin-nav {
		display: flex;
		align-items: center;
		gap: 2rem;
		padding: 1rem 2rem;
		background: var(--ink-soft);
		border-bottom: 1px solid rgba(245, 240, 232, 0.07);
		position: sticky;
		top: 0;
		z-index: 10;
	}

	.admin-logo {
		font-family: var(--f-display);
		font-weight: 800;
		font-size: 1rem;
		color: var(--white);
		letter-spacing: 0.05em;
		margin-right: auto;
	}

	.admin-logo span { color: var(--amber); }

	.admin-links {
		display: flex;
		gap: 1.5rem;
	}

	.admin-link {
		font-family: var(--f-display);
		font-size: 0.75rem;
		font-weight: 600;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--muted);
		transition: color 0.2s;
		padding-bottom: 2px;
	}

	.admin-link:hover, .admin-link.active {
		color: var(--amber-bright);
		border-bottom: 1px solid var(--amber);
	}

	.btn-logout {
		font-family: var(--f-display);
		font-size: 0.7rem;
		font-weight: 600;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--muted);
		background: none;
		border: 1px solid rgba(245, 240, 232, 0.12);
		border-radius: 2px;
		padding: 0.35rem 0.75rem;
		cursor: pointer;
		transition: color 0.2s;
	}

	.btn-logout:hover { color: var(--paper); }

	/* ── Page content ── */
	.admin-main {
		padding: 2.5rem 2rem;
		flex: 1;
	}

	.page-header {
		display: flex;
		align-items: flex-start;
		justify-content: space-between;
		margin-bottom: 2rem;
		gap: 1rem;
	}

	.page-title {
		font-family: var(--f-display);
		font-weight: 700;
		font-size: 1.5rem;
		color: var(--white);
	}

	.count-badge {
		font-size: 0.75rem;
		color: var(--amber);
		font-family: var(--f-display);
		font-weight: 600;
		letter-spacing: 0.08em;
		margin-top: 0.25rem;
	}

	.btn-export {
		font-family: var(--f-display);
		font-size: 0.75rem;
		font-weight: 700;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		padding: 0.6rem 1.25rem;
		background: rgba(212, 134, 10, 0.1);
		color: var(--amber-bright);
		border: 1px solid var(--border);
		border-radius: 2px;
		cursor: pointer;
		transition: background 0.2s;
		white-space: nowrap;
	}

	.btn-export:hover:not(:disabled) { background: rgba(212, 134, 10, 0.2); }
	.btn-export:disabled { opacity: 0.4; cursor: not-allowed; }

	/* ── States ── */
	.admin-loading, .admin-empty {
		font-size: 0.9rem;
		color: var(--muted);
		padding: 3rem 0;
	}

	.admin-error {
		color: #e05252;
		font-size: 0.9rem;
		padding: 1rem;
		border: 1px solid rgba(224, 82, 82, 0.3);
		border-radius: 2px;
	}

	/* ── Table ── */
	.table-wrap {
		overflow-x: auto;
		border: 1px solid rgba(245, 240, 232, 0.07);
		border-radius: 4px;
	}

	table {
		width: 100%;
		border-collapse: collapse;
		font-size: 0.875rem;
	}

	thead {
		background: var(--ink-soft);
	}

	th {
		text-align: left;
		padding: 0.75rem 1rem;
		font-family: var(--f-display);
		font-size: 0.65rem;
		font-weight: 700;
		letter-spacing: 0.15em;
		text-transform: uppercase;
		color: var(--muted);
		border-bottom: 1px solid rgba(245, 240, 232, 0.07);
	}

	td {
		padding: 0.85rem 1rem;
		color: var(--paper-dim);
		border-bottom: 1px solid rgba(245, 240, 232, 0.04);
	}

	tr:last-child td { border-bottom: none; }
	tr:hover td { background: rgba(245, 240, 232, 0.02); }

	.email-link {
		color: var(--amber-bright);
	}

	.email-link:hover { text-decoration: underline; }

	.profile-badge {
		font-size: 0.72rem;
		font-family: var(--f-display);
		font-weight: 600;
		letter-spacing: 0.06em;
		color: var(--amber);
		background: rgba(212, 134, 10, 0.08);
		border: 1px solid rgba(212, 134, 10, 0.2);
		border-radius: 2px;
		padding: 0.2rem 0.5rem;
	}

	.date-cell {
		color: var(--muted);
		font-size: 0.8rem;
	}
</style>
