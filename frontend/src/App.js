import ReactHLSPlayer from 'react-hls-player';

import './App.css';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Video Test</h1>
          <ReactHLSPlayer
            url="http://localhost:8000/streams/vid.m3u8"
            autoplay={true}
            controls={true}
            width={600}
            hlsConfig={{
              // liveDurationInfinity: true,
              // liveBackBufferLength: 0,
              // liveMaxLatencyDurationCount: 6,
            }}
          />
      </header>
    </div>
  );
}

export default App;
