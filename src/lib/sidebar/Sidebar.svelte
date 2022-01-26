<nav>
	{#each routes as route}
		{#if route.path === '/'}
			<Route {route}>poop</Route>
		{:else}
			<Route {route} />
		{/if}
	{/each}
</nav>

<style>
	nav {
		@apply bg-gray-50 border-gray-300 md:border-r <md:border-b;
	}
</style>

<script lang="ts">
	import routes from '../routes'
	import Route from './Route.svelte'
</script>
