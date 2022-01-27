<div class:md:hidden={!offsetWidth}>
	<div class="offset" style:--offset="{offsetWidth}px">💻 Software Developer</div>

	{#each featuredSkills as skill}
		<details open on:click|preventDefault={() => onClick(skill.name)}>
			<summary class="offset" style:--offset="{offsetWidth}px">
				{skill.name}
			</summary>

			{#if active === skill.name}
				<ul class="bg-gray-50" transition:slide>
					{#each skill.works as work}
						<li>{work.title}</li>
					{/each}
				</ul>
			{/if}
		</details>
	{/each}
</div>

<style>
	@screen md {
		.offset {
			margin-left: calc(var(--offset) + 1rem);
		}
	}

	summary {
		display: inline-block;
	}

	summary::-webkit-details-marker {
		display: none;
	}
</style>

<script lang="ts">
	import { skillsWithWorks } from '$lib/skills'
	import { slide } from 'svelte/transition'

	export let offsetWidth: number

	let featuredSkills = skillsWithWorks
		.filter(({ featured, works }) => featured && works.length > 0)

	let active: string | false = false

	function onClick(name: string) {
		if (active === name) {
			active = false
		} else {
			active = name
		}
	}
</script>
