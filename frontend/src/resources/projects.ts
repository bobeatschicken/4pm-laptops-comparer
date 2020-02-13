import { useCallback, useEffect } from "react"
import { navigate } from "@reach/router"
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

export function useCreateWorkspace() {
  const { token } = useAuth()

  const [{ data }, run] =
    useAxios({
      url: `${BASE_URL}/workspaces`,
      method: "POST",
      headers: {
        Authorization: token
      }
    }, { manual: true })

  useEffect(() => {
    if (data) {
      navigate(`/app/workspace/${data._id}`)
    }
  }, [data])

  return useCallback(() => {
    run()
  }, [run])
}

export function useWorkspace(workspaceId: string) {
  const { token, loaded } = useAuth()

  const [{ data, error }, run] =
    useAxios({
      url: `${BASE_URL}/workspaces/${workspaceId}`,
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
    data,
    error: data?.error,
    loading: !data && !error
  }
}
