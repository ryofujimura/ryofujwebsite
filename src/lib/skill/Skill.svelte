<article>
	{skill.name}

	<progress min={0} max={10} value={skill.level} title="{skill.level} / 10" />
</article>

<style>
	article {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		align-items: center;
	}

	progress {
		width: 100%;
		height: 0.5ch;

		@apply bg-gray-100;
	}

	progress::-webkit-progress-bar {
		@apply bg-gray-100;
	}

	progress::-webkit-progress-value {
		@apply bg-amber-500;
	}

	progress::-moz-progress-bar {
		@apply bg-amber-500;
	}
</style>

<script lang="ts">
	export let skill: Skill
</script>
