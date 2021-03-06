import consts from "../main/consts";
import axios from 'axios';


export const changeMessage = event => ({
    type: 'MESSAGE_CHANGED',
    payload: event.target.value
})


export const getMessages = () => {
    let session_id = localStorage.getItem(consts.USER_SESSION);

    if (session_id == 'undefined')
        session_id = ''

    const request = axios.get(`${consts.BASE_URL_API}/page_chat${session_id}`)

    return{
        type: 'CHAT_MESSAGES_FETCHED',
        payload: request
    }
}


export const storeUser = (request) => {
    console.log(request.data)
    return {
        type: 'USER_OBTAINED',
        payload: request
    }
}


export const clear = () => {
    return {
        type: 'MESSAGE_SENT'
    }
}

export const newMessage = () => {
    return { type: 'NEW_MESSAGE'}
}


export const getCart = () => {
    let session_id = localStorage.getItem(consts.USER_SESSION);

    if (session_id == 'undefined')
        session_id = ''

    
    const request = axios.get(`${consts.BASE_URL_API}/page_chat${session_id}`)

    return {
        type: 'CART_FETCHED',
        payload: request
    }
}

export const sendMessage = (message) => {
    const session_id = localStorage.getItem(consts.USER_SESSION);

    return dispatch => {
        dispatch(newMessage());
        dispatch(clear());
        axios.post(`${consts.BASE_URL_API}/page_chat`, {message, session_id})
            .then(res => dispatch(storeUser(res)))
            .then(() => dispatch(getCart()))
            .then(() => dispatch(getMessages()))
    }


}