import axios from 'axios'
import router from '@/router'


const AUTH_LOGIN_URL = 'http://localhost:5000/api/v1/users/login'; // no trailing slash

const state = {
    email: null,
    username: null,
    token: null,
};

const mutations = {
    authUser(state, userData) {
        state.email = userData.email;
        state.token = userData.token;
    },
    clearAuthData(state) {
        state.email = null;
        state.token = null;
    },
};

const getters = {
    isAuthenticated(state) {
        return state.token !== null;
    },
};

const actions = {
    login: ({commit}, authData) => {
        axios.post(AUTH_LOGIN_URL, authData).then(response => {
            let success = response.data.success;
            if (success === true) {
                commit('authUser', {email: authData.email, token: response.data.token});
                localStorage.setItem('email', authData.email);
                localStorage.setItem('token', response.data.token);
                router.replace('dashboard');
            } else {
                console.log('Login error');
            }
        }).catch(error => {
            console.log(error);
        })
    },
    logout: ({commit}) => {
        commit('clearAuthData');
        localStorage.removeItem('email');
        localStorage.removeItem('token');
        router.replace('logout');
    },
};

export default {
    namespaced: true,
    state,
    mutations,
    getters,
    actions,
}
