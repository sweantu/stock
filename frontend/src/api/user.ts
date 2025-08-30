import apiClient from './index'

const getMany = async () => {
  const { data } = await apiClient.get('/admin/users')
  return data
}
const create = (data) => apiClient.post('/admin/users', data)

export { create, getMany }
