<nav class="bg-gray-50 border-gray-300 md:border-r <md:border-b">
	<Logo route={home} />
	<Routes routes={rest} />
	<Links/>
</nav>

<style>
	nav {
		grid-area: sidebar;
		display: flex;
		flex-direction: column;
		gap: 1rem;
		padding: 1rem;
	}
</style>

<script lang="ts">
	import routes from '../routes'
	import Logo from './Logo.svelte'
	import Routes from './Routes.svelte'
	import Links from './Links.svelte'

	let [home, ...rest] = routes.filter(({ featured }) => featured)
</script>
