<li class:active>
	<Title {path} />
	<CloseTab {path} {active} />
</li>

<style>
	li {
		display: inline-flex;
		align-items: center;

		@apply border-t border-x border-gray-300 text-gray-500;
	}

	li:not(:first-child) {
		margin-left: -1px;
	}

	@screen md {
		li:first-child {
			border-left: 0;
		}
	}

	li:hover,
	.active {
		background-color: #fff;
		color: #000;
	}

	li:not(:hover):not(.active) :global(.close) {
		pointer-events: none;
		opacity: 0;
	}

	.active {
		position: sticky;
		left: 0;
		right: 0;
		z-index: 1;

		@apply border-t-amber-500;
	}

	.active::after {
		content: '';
		position: absolute;
		top: 100%;
		left: 0;
		right: 0;
		border-bottom: 1px solid #fff;
	}
</style>

<script lang="ts">
	import Title from './Title.svelte'
	import { page } from '$app/stores'
	import CloseTab from './CloseTab.svelte'

	export let path: Path

	$: active = $page.url.pathname === path
</script>
