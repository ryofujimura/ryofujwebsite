<nav>
	<Logo route={home} />

	<ul>
		{#each rest as route}
			<li>
				<Route {route} />
			</li>
		{/each}
	</ul>
</nav>

<style>
	nav {
		display: flex;
		flex-direction: column;
		padding: 1rem;

		@apply bg-gray-50 border-gray-300 md:border-r <md:border-b;
	}

	ul {
		margin-block: auto;
	}
</style>

<script lang="ts">
	import routes from '../routes'
	import Logo from './Logo.svelte'
	import Route from './Route.svelte'

	let [home, ...rest] = routes
</script>
