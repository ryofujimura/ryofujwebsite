<ul class="bg-gray-50 border-b border-gray-300 no-scrollbar">
	{#each $tabs as tab (tab)}
		<Tab path={tab} />
	{:else}
		<Tab path="/" />
	{/each}
</ul>

<style>
	ul {
		position: sticky;
		top: 0;
		left: 0;
		display: flex;
		padding-top: 0.25rem;
		overflow-x: auto;
		overflow-y: hidden;
		max-width: 100vw;
	}

	ul::after {
		content: '';
		border-right: 1px solid transparent;
		margin-right: -1px;
	}
</style>

<script lang="ts">
	import { tabs } from '$lib/store'
	import Tab from './Tab.svelte'
</script>
