import React, { Component } from 'react'
import ProdutosList from './produtos/produtosList';

class Dashboard extends Component{
    render(){
        return(
            <div className="container">
                <div className="inner cover">
                    <h1 className="cover-heading"> Conheça nossos produtos.</h1>
                    <p className="lead">Basta pedir no chat abaixo e adicionaremos o produto no carrinho para você</p>

                    <ProdutosList />

                </div>

                
            </div>


        )
    }
}

export default Dashboard