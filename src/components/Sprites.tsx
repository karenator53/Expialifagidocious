import { useEffect, useRef } from 'react';

interface SpriteProps {
  name: 'sparkle' | 'burst' | 'fade';
  x: number;
  y: number;
  onComplete?: () => void;
}

export function Sprite({ name, x, y, onComplete }: SpriteProps) {
  const spriteRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const element = spriteRef.current;
    if (!element) return;

    element.style.left = `${x}px`;
    element.style.top = `${y}px`;
    
    const animationEndHandler = () => {
      if (onComplete) {
        onComplete();
      }
      element.remove();
    };

    element.addEventListener('animationend', animationEndHandler);
    return () => element.removeEventListener('animationend', animationEndHandler);
  }, [x, y, onComplete]);

  return <div ref={spriteRef} className={`sprite sprite--${name}`} />;
}

export function createSprite(name: SpriteProps['name'], x: number, y: number) {
  const sprite = document.createElement('div');
  sprite.className = `sprite sprite--${name}`;
  sprite.style.left = `${x}px`;
  sprite.style.top = `${y}px`;
  document.body.appendChild(sprite);

  sprite.addEventListener('animationend', () => {
    sprite.remove();
  });
}