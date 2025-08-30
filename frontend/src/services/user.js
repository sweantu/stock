// services/user.js
import api from './api'

const getMany = async () => {
  const { data } = await api.get('/admin/users')
  return data
}
const create = (data) => api.post('/admin/users', data)

export { getMany, create }
