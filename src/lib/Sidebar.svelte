<nav>
	{#each routes as route}
		<a href={route.path} on:click={() => onClick(route.path)}>
			{route.title}
		</a>
	{/each}
</nav>

<style>
	nav {
		@apply bg-gray-50 border-gray-300 md:border-r <md:border-b;
	}

	a {
		display: block;
	}
</style>

<script lang="ts">
	import routes from './routes'
	import { tabs } from '$lib/store'
	import { browser } from '$app/env'

	function onClick(path: Path): void {
		if (!$tabs.includes(path)) {
			$tabs.push(path)

			if (browser) {
				window.localStorage.setItem('tabs', JSON.stringify($tabs))
			}
		}
	}
</script>
