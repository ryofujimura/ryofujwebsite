<ul>
	{#each routes as route}
		<li>
			<Route {route} />
		</li>
	{/each}
</ul>

<style>
	ul {
		margin-block: auto;
	}
</style>

<script lang="ts">
	import Route from './Route.svelte'

	export let routes
</script>
