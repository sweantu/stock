// services/user.js
import api from './api'

const getMany = () => api.get('/admin/users')
const create = (data) => api.post('/admin/users', data)

export { getMany, create }
