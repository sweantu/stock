import { storeToRefs } from 'pinia'

export function useCounter() {
  const counterStore = useCounterStore()
  const { count } = storeToRefs(counterStore)

  const increment = () => counterStore.increment()

  return {
    count,
    increment,
  }
}
