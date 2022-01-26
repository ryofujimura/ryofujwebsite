<ul class="no-scrollbar">
	{#each $tabs as tab}
		<Tab path={tab} />
	{:else}
		<Tab path="/" />
	{/each}
</ul>

<style>
	ul {
		display: flex;
		padding-top: 0.25rem;
		overflow-x: auto;
		overflow-y: hidden;
		max-width: 100vw;

		@apply bg-gray-50 border-b border-gray-300;
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
