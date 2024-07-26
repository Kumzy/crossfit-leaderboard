<script setup lang="ts">
// Define the props interface
interface MenuItem {
  icon: string
  label: string
  url: string
  route: string
  href: string
}

interface Props {
  menuItems: MenuItem[]
}
// Use defineProps to declare props
// const items = defineProps<Props>();

const items: MenuItem[] = [
  { icon: "path/to/icon1.png", label: "Home", url: "/" },
  { icon: "path/to/icon2.png", label: "About", url: "/about" },
  { icon: "path/to/icon3.png", label: "Contact", url: "/contact" },
]
</script>

<template>
  <Menu :model="items">
      <template #item="{ item, props }">
          <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
              <a v-ripple :href="href" v-bind="props.action" @click="navigate">
                  <span :class="item.icon" />
                  <span class="ml-2">{{ item.label }}</span>
              </a>
          </router-link>
          <a v-else v-ripple :href="item.url" :target="item.target" v-bind="props.action">
              <span :class="item.icon" />
              <span class="ml-2">{{ item.label }}</span>
          </a>
      </template>
  </Menu>
</template>

<style scoped>

</style>
