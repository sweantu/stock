// services/user.js
import api from './api'

export const getUsers = () => api.get('/admin/users')
export const createUser = (data) => api.post('/admin/users', data)
