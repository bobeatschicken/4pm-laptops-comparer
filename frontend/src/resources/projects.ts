import { useEffect } from "react"
import { useAuth } from "utils/auth"
import useAxios from "axios-hooks"

const BASE_URL = process.env.REACT_APP_API_ENDPOINT

export function useWorkspaces() {
  const { token, loaded } = useAuth()

  const [{ data, error }, run] =
    useAxios({
      url: `${BASE_URL}/workspaces`,
      headers: {
        Authorization: token
      }
    }, { manual: true })

  useEffect(() => {
    if (loaded) {
      if (token) {
        run()
      }
    }
  }, [loaded, run, token])

  return {
    workspaces: data?.workspaces || [],
    error: data?.error,
    loading: !data && !error
  }
}
