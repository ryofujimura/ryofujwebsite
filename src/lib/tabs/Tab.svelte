<li>
	{#if route?.title}
		<a href={route.path}>{route.title}</a>
	{:else}
		Blank
	{/if}

	<button on:click={close}>×</button>
</li>

<style>
	li {
		display: inline-block;

		@apply border border-b-0 border-gray-300;
	}
</style>

<script lang="ts">
	import routes from '$lib/routes'
	import { tabs } from '$lib/store'
	import { browser } from '$app/env'
	import { page } from '$app/stores'
	import { goto } from '$app/navigation'

	export let path: Path | null = null

	$: route = routes.find(route => route.path === path)

	function close(): void {
		let filtered = $tabs.filter(tab => tab !== path)
		$tabs = filtered

		if (browser) {
			window.localStorage.setItem('tabs', JSON.stringify($tabs))
		}

		// update content to first tab or homepage if closed tab was active
		if ($page.url.pathname === path) {
			goto($tabs[0] || '/')
		}
	}
</script>
