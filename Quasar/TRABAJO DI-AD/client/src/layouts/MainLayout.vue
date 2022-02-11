<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn flat dense round icon="menu" aria-label="Menu" @click="toggleLeftDrawer" />

        <q-toolbar-title>Sistema de notas</q-toolbar-title>

        <div>{{ dataActual }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" >
      <q-list>

        <EssentialLink v-for="link in essentialLinks" :key="link.title" v-bind="link" />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue'

const linksList = [
  {
    title: 'Login',
    caption: 'Iniciar sesión',
    icon: 'login',
    link: '#/Login'
  },
  {
    title: 'About',
    caption: 'About',
    icon: 'contact_support',
    link: '#/About'
  }
]

import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink
  },

  setup () {
    const leftDrawerOpen = ref(false)

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  },
  computed: {
    dataActual () {
      const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
      const dateAct = new Date().toLocaleDateString('ca-Es', options)
      return dateAct.toLocaleUpperCase()
    }
  }
})
</script>
