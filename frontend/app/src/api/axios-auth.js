import axios from 'axios'

const instance = axios.create({
    baseURL: process.env.API_URL || 'http://localhost:5000/api/v1',

});

instance.interceptors.request.use(
    (config) => {
        let token = localStorage.getItem('token');

        if (token) {
            config.headers['withCredentials'] = true;
            config.headers['api-token'] = localStorage.getItem('token');
            config.headers['Content-Type'] = 'application/json'
            console.log("passing in here", config);
        }
        return config
    },

    (error) => {
        return Promise.reject(error)
    }
)


export default instance
