import Cookies from 'js-cookie'
export const API_URL = "http://localhost:3000/api/v1/"

export const API = {
    csfr: API_URL + 'csrf_token/',
    submit: (id) => API_URL + `submit/${id}/`,
}

export function getHeaders() {
    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-CSRFToken': Cookies.get('csrftoken')
    }
}

