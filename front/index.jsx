import 'commons.styl';
import React from 'react';
import ReactDOM from 'react-dom'


class Main extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            items: []
        }
    }

    componentDidMount() {
        
    }

    render() {
        return (
            <div className="app">
                <div id="header">
                    <img className="logo" src="//codeforseoul.org/jonmat/static/logo.png" />
                </div>
                <div>
                    <div>존맛 국회는</div>
                </div>
                <div>
                    <div className="by-congress">
                        <h3>인기 정치인</h3>
                        <ul>
                            <li>asd</li>
                        </ul>
                    </div>
                    <div className="by-store">
                        <h3>인기 음식점</h3>
                        <ul>
                            <li>qwasdasd</li>
                        </ul>
                    </div>
                </div>
            </div>
        )
    }
}


ReactDOM.render(<Main />, document.getElementById('main'));
