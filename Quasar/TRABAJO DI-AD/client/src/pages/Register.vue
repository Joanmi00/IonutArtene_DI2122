<template>
  <q-page class="bg-light-gray window-height window-width row justify-center items-center">
    <div class="column">
      <div class="row">
        <h5 class="text-h5 text-gray q-my-md">Registrate</h5>
      </div>
      <div class="row">
        <q-card square bordered class="q-pa-lg shadow-1">
          <q-card-section>
            <q-form class="q-gutter-md">
              <q-input
              lazy-rules
              :rules="[ valor => valor && isValidDni && valor.length==9 || 'Formato incorrecto']"
              square filled clearable v-model="dni" type="" label="DNI"/>
              <q-input
              lazy-rules
              :rules="[ valor =>valor && isValidNom || 'Formato incorrecto']"
              square filled clearable v-model="nom" type="" label="Nom" />
              <q-input
              lazy-rules
              :rules="[ valor => valor && valor.length > 0 || 'Este campo no puede estar vacio']"
              square filled clearable v-model="usuari" type="email" label="Usuari" />
              <q-input
              lazy-rules
              :rules="[ valor => valor && valor.length > 0 || 'Este campo no puede estar vacio']"
              square filled clearable v-model="contrasenya1" type="password" label="Contrasenya" />
              <q-input
              lazy-rules
              :rules="[ valor => valor && valor.length > 0 || 'Este campo no puede estar vacio']"
              square filled clearable v-model="contrasenya2" type="password" label="Escribe de nuevo la contraseña" />
            </q-form>
          </q-card-section>
          <q-card-actions class="q-px-md">
            <q-btn unelevated color="primary" size="lg" class="full-width" label="Iniciar sesión" />
          </q-card-actions>
          <q-card-section class="text-center q-pa-none q-px-md">
            <p class="text-grey-6">Ya tienes cuenta? <a href="#/">Inicia sesión</a></p>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'Register',
  data () {
    return {
      nom: '',
      dni: '',
      usuari: '',
      contrasenya1: '',
      contrasenya2: ''
    }
  },
  computed: {
    isValidDni () {
      const refExp = /[0-9]{8}[A-Za-z]/
      return refExp.test(this.dni)
    },
    isValidNom () {
      const noms = this.nom.slice(' ')
      if (noms[0].length > 3 && noms[1].length > 3) {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style>
.q-card {
  width: 360px;
}
</style>
