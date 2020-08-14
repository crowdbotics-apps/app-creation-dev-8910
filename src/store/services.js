import axios from "axios"
const aUTHTEST = axios.create({
  baseURL: "https://a.com",
  headers: { Accept: "application/json", "Content-Type": "application/json" }
})
export const apiService = {}
