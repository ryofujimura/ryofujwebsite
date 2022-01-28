<div class:md:hidden={!offsetWidth}>
	<div class="title" style:--offset="{offsetWidth}px">
		💻 Software Developer
	</div>

	{#each featuredSkills as skill}
		<details open={$activeFeaturedSkill === skill.name}>
			<summary
				class="title"
				style:--offset="{offsetWidth}px"
				on:click|preventDefault={() => onClick(skill.name)}
			>
				{skill.name}
			</summary>

			<FeaturedWorks works={skill.works} />
		</details>
	{/each}
</div>

<style>
	.title {
		@apply leading-10;
	}

	@screen md {
		.title {
			margin-left: calc(var(--offset) + 2rem);
		}
	}

	summary {
		user-select: none;
		position: relative;
		display: inline-block;
		outline: 0;
	}

	summary::-webkit-details-marker {
		display: none;
	}

	details[open] summary::before {
		content: '';
		position: absolute;
		left: 0;
		top: 100%;
		transform: rotate(45deg) scale(0.5);
		display: inline-block;
		border: 1em solid theme('colors.gray.100');
	}
</style>

<script lang="ts">
	import { skillsWithWorks } from '$lib/skills'
	import { activeFeaturedSkill, localStore } from '$lib/store'
	import FeaturedWorks from './FeaturedWorks.svelte'

	export let offsetWidth: number

	let featuredSkills = skillsWithWorks
		.filter(({ featured, works }) => featured && works.length > 0)

	function onClick(name: string) {
		if ($activeFeaturedSkill === name) {
			$activeFeaturedSkill = null
		} else {
			$activeFeaturedSkill = name
		}

		localStore('activeFeaturedSkill', $activeFeaturedSkill)
	}
</script>
