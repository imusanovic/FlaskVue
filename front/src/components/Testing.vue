<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Ljudovi</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.user-modal>Dodaj ljudova</button>
        <br><br>
        <alert></alert>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Ime</th>
              <th scope="col">Prezime</th>
              <th scope="col">Adresa</th>
              <th scope="col">Mobitel</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(user, index) in data" :key="index">
              <td>{{ user.ime }}</td>
              <td>{{ user.prezime }}</td>
              <td>{{ user.adresa.ulica }} {{ user.adresa.broj }} {{ user.adresa.grad }}</td>
              <td>{{ user.mobitel }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
        <!-- Modal za dodavanje novog ljudova -->
        <b-modal ref="addUserModal"
                 id="user-modal"
                 title="Dodaj novog ljudova"
                 hide-footer>
            <b-form @submit="onSubmit" @reset="onReset" class="w-100">
            <b-form-group id="form-ime-group"
                        label="Ime:"
                        label-for="form-ime-input">
                <b-form-input id="form-ime-input"
                            type="text"
                            v-model="dodajLjudovaForm.ime"
                            required
                            placeholder="Unesi ime ljudova">
                </b-form-input>
            </b-form-group>
            <b-form-group id="form-prezime-group"
                        label="Prezime:"
                        label-for="form-prezime-input">
                <b-form-input id="form-prezime-input"
                            type="text"
                            v-model="dodajLjudovaForm.prezime"
                            required
                            placeholder="Unesite prezime ljudova">
                </b-form-input>
            </b-form-group>
            <b-form-group id="form-ulica-group"
                          label="Ulica:"
                          label-for="form-ulica-input">
                <b-form-input id="form-ulica-input"
                              type="text"
                              v-model="dodajLjudovaForm.ulica"
                              required
                              placeholder="U kojoj ulici živi ljudov?">
                </b-form-input>
            </b-form-group>
            <b-form-group id="form-broj-group"
                          label="Broj:"
                          label-for="form-broj-input">
                <b-form-input id="form-broj-input"
                              type="text"
                              v-model="dodajLjudovaForm.broj"
                              required
                              placeholder="Ljudovljev kućni broj?">
                </b-form-input>
            </b-form-group>
            <b-form-group id="form-grad-group"
                          label="Grad:"
                          label-for="form-grad-input">
                <b-form-input id="form-grad-input"
                              type="text"
                              v-model="dodajLjudovaForm.grad"
                              required
                              placeholder="Grad?">
                </b-form-input>
            </b-form-group>
            <b-form-group id="form-mobitel-group"
                          label="Mobitel:"
                          label-for="form-mobitel-input">
                <b-form-input id="form-mobitel-input"
                              type="text"
                              v-model="dodajLjudovaForm.mobitel"
                              required
                              placeholder="Na koji zoveš ljudova?">
                </b-form-input>
            </b-form-group>
            <b-button type="submit" variant="primary">Dodaj ljudova</b-button>
            <b-button type="reset" variant="danger">'Ajmo ispočetka</b-button>
          </b-form>
        </b-modal>
  </div>
</template>

<style>
    #app{
        margin-top:60px;
    }
</style>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  name: 'Test',
  data() {
    return {
      data: [],
      dodajLjudovaForm: {
        ime: '',
        prezime: '',
        adresa: {
            ulica: '',
            broj: '',
            grad: ''
        },
        mobitel: ''
      }
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    sviLjudovi() {
        const endpoint = '//localhost:5000/users'
        axios.get(endpoint).then((res) => {
            this.data = res.data.users;
        })
        .catch((error) => {
            console.error(error);
        })
    },
    dodajLjudova(payload){
        const endpoint = '//localhost:5000/users'
        axios.post(endpoint, payload).then(() => {
            this.sviLjudovi();
        })
        .catch((error) => {
            console.log(error);
            this.sviLjudovi();
        });
    },
    initForm(){
        this.dodajLjudovaForm.ime = '';
        this.dodajLjudovaForm.prezime = '';
        this.dodajLjudovaForm.ulica = '';
        this.dodajLjudovaForm.broj = '';
        this.dodajLjudovaForm.grad = '';
        this.dodajLjudovaForm.mobitel = '';
    },
    onSubmit(evt){
        evt.preventDefault();
        this.$refs.addUserModal.hide();
        const payload = {
            ime: this.dodajLjudovaForm.ime,
            prezime: this.dodajLjudovaForm.prezime,
            adresa: {
                ulica: this.dodajLjudovaForm.ulica,
                broj: this.dodajLjudovaForm.broj,
                grad: this.dodajLjudovaForm.grad
            },
            mobitel: this.dodajLjudovaForm.mobitel
        }
        console.log(payload);
        this.dodajLjudova(payload);
        this.initForm();
    },
    onReset(){
        evt.preventDefault();
        this.$refs.addUserModal.hide();
        this.initForm();
    }
  },
  created(){
    this.sviLjudovi();
  }
};
</script>
