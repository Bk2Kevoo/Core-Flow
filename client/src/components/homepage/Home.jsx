import styled from 'styled-components';

function Home() {
  return (
    <HomeContainer>
      <Overlay>
        <WelcomeMessage>
          <h1>Welcome to Core Flow</h1>
          <p>Your journey to fitness and wellness begins here.</p>
        </WelcomeMessage>
      </Overlay>
    </HomeContainer>
  );
}

export default Home;

const HomeContainer = styled.div`
  height: 100vh;
  width: 100%;
  // background: url('/path-to-your-image-or-gif.gif') no-repeat center center/cover;
  display: flex;
  align-items: center;
  justify-content: center;
`;

const Overlay = styled.div`
  background-color: rgba(0, 0, 0, 0.5); /* Slightly lighter overlay */
  height: 100%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
`;

const WelcomeMessage = styled.div`
  text-align: center;
  color: #fff;

  h1 {
    font-size: 2rem; /* Reduced font size */
    margin-bottom: 0.5rem; /* Smaller spacing between header and paragraph */
  }

  p {
    font-size: 1rem; /* Reduced paragraph font size */
    max-width: 400px; /* Narrower text area */
    margin: 0 auto;
  }
`;
