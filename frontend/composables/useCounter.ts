import { storeToRefs } from 'pinia'
import { useCounterStore } from '~/stores/counter'

export function useCounter() {
  const counterStore = useCounterStore()
  const { count } = storeToRefs(counterStore)

  const increment = () => counterStore.increment()

  return {
    count,
    increment,
  }
}
