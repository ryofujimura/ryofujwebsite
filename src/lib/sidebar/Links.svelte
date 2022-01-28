<ul>
	<li>
		<a href={site.github} target="_blank" rel="noopener" title="GitHub @ryofuj">
			<GitHubIcon/>
		</a>
	</li>
</ul>

<style>
	ul {
		display: flex;
		align-items: center;
		justify-content: center;
	}

	ul :global(svg) {
		font-size: 1.2em;
	}
</style>

<script lang="ts">
	import GitHubIcon from '$lib/icon/GitHub.svelte'
	import site from '$lib/site'
</script>
