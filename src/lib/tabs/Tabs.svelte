<ul>
	{#each $tabs as tab}
		<Tab path={tab} />
	{:else}
		<Tab path="/" />
	{/each}
</ul>

<style>
	ul {
		@apply bg-gray-50 border-b border-gray-300;
	}
</style>

<script lang="ts">
	import { tabs } from '$lib/store'
	import Tab from './Tab.svelte'
</script>
