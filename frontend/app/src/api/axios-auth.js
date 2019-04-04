import axios from 'axios'

const instance = axios.create({
    baseURL: 'http://localhost:5000/api',
    headers: {
        'Authorization': {
            toString() {
                return `Bearer ${localStorage.getItem('token')}`
            }
        }
    }
});

export default instance
