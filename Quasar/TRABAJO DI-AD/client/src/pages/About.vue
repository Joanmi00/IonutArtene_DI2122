<template>
  <q-page class="bg-gray window-height window-width row q-pa-xl ">
     <div class="column">
      <div class="row"  >
      <h2 style="font-size: 20vh">About</h2>
      </div>
        <div class="row"  >
        <h5 class="text-h5" style="opacity:.4">Es una App destinada al control de las notas en las asignaturas del curso.<br/>
       Proyecto hecho en conjunto en las asignaturas DI-AD del IES El Just de Tavernes de La Valldigna
       </h5>
      </div>
     </div>
  </q-page>
</template>

<script>
export default {
  name: 'About',
  data () {
    return {
      usuari: '',
      contrasenya: ''
    }
  }
}

</script>
