<template>
  <q-page class="bg-light-gray window-height window-width row justify-center items-center">
    <div class="column">
      <div class="row">
        <h5 class="text-h5 text-gray q-my-md">Iniciar sesión</h5>
      </div>
      <div class="row">
        <q-card square bordered class="q-pa-lg shadow-1">
          <q-card-section>
            <q-form class="q-gutter-md">
              <q-input
               lazy-rules
              :rules="[ valor => valor && valor.length >=5 || 'Formato incorrecto']"
              square filled clearable v-model="usuari" type="email" label="Usuario" />
              <q-input
               lazy-rules
              :rules="[ valor => valor && valor.length > 0 || 'Este campo no puede estar vacio']"
              square filled clearable v-model="contrasenya" type="password" label="Contraseña" />
            </q-form>
          </q-card-section>
          <q-card-actions class="q-px-md">
            <q-btn unelevated color="primary" size="lg" class="full-width" label="Iniciar sesión" />
          </q-card-actions>
          <q-card-section class="text-center q-pa-none q-px-md">
            <p class="text-grey-6">No tienes cuenta? <a href="#/Register">Registrate</a></p>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      usuari: '',
      contrasenya: ''
    }
  }
}

</script>

<style>
.q-card {
  width: 360px;
}
</style>
